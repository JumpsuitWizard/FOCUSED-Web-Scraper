import React, { useState, useEffect } from "react";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import Dashboard from "./components/Dashboard";

export default function App() {
  const [selectedLink, setSelectedLink] = useState("home");
  const [data, setData] = useState(null); 

  const componentsMap = {
    home: <Home data={data}/>,
    dashboard: <Dashboard />
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
 
        const response = await fetch("http://127.0.0.1:4000/dependencies");
        const data = await response.json();
        const transformedData = data.components.reduce((result, item, index) => {
          const companyName = item.company.name;
          const existingIndex = result.findIndex((entry) => entry.company_name === companyName);
        
          if (existingIndex !== -1) {
            result[existingIndex].packages.add(item.name);
          } else {
            result.push({ index: index + 1, company_name: companyName, packages: new Set([item.name]) });
          }
        
          return result;
        }, []);
        
        console.log(transformedData);
        
        setData(transformedData); 
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData(); 

    
  }, []);

  return (
    <div style={{ margin: 0, padding: 0, width: "100%", height: "100%" }}>
      <Navbar selectedLink={selectedLink} setSelectedLink={setSelectedLink} />
      <div className="mt-16">
       {/* Check if data is available before rendering */}
       {data ? componentsMap[selectedLink] : <p>Loading...</p>}
      </div>
    </div>
  );
}