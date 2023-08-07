import React, { useState, useEffect } from "react";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import Dashboard from "./components/Dashboard";
import { Route, Routes } from "react-router-dom";
import CompanyDetails from "./components/CompanyDetails";
import Loader from "./components/Loader";

export default function App() {
  const [searchTerm, setSearchTerm] = useState("");
  const [data, setData] = useState(null); 
  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
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
        
        setData(transformedData); 
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData(); 

    
  }, []);
    
  const filteredData =
    data &&
    data.filter((value) =>
      value.company_name.includes(searchTerm.toLowerCase())
    );


  return (
    <div style={{ margin: 0, padding: 0, width: "100%", height: "100%" }}>
      <Navbar searchTerm={searchTerm} handleSearch={handleSearch} /> 
        {data === null ? <Loader />:
        <Routes>
          <Route path="/" exact element = { <Home data={filteredData} searchTerm ={searchTerm} /> }/>
          <Route path="dashboard" exact element={ <Dashboard /> }/>
          <Route path="/company/:companyName" exact element={ <CompanyDetails /> }/>
        </Routes>}
      </div>
  );
}