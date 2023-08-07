import React, { useState, useEffect } from "react";
import Tab from "./Tab";
import Companies from "./Companies";
import Dependencies from "./Dependencies";

const Home = ({ data, searchTerm }) => {
  const [selectedTab, setSelectedTab] = useState("Companies");
  const [dependenciesData, setDependenciesData] = useState();

  const handleTabSelect = (title) => {
    setSelectedTab(title);
  };
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:4000/dependencies/packages`
        );
        const data = await response.json();

        const transformedData = data.components;

        // Sort the array based on the number of shared_authors in descending order
        transformedData.sort(
          (a, b) => b.shared_authors.length - a.shared_authors.length
        );

        setDependenciesData(transformedData);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  const filteredData =
    dependenciesData &&
    dependenciesData.filter((value) =>
      value.name.includes(searchTerm.toLowerCase())
    );
  return (
    <>
      <div className="mt-16 ml-20">
        <div className="flex">
          <Tab
            title="Companies"
            selected={selectedTab === "Companies"}
            onSelect={handleTabSelect}
          />
          <Tab
            title="Dependencies"
            selected={selectedTab === "Dependencies"}
            onSelect={handleTabSelect}
          />
        </div>
        {selectedTab === "Companies" && <Companies data={data} />}
        {selectedTab === "Dependencies" && filteredData && (
          <Dependencies data={filteredData} />
        )}
      </div>
    </>
  );
};

export default Home;
