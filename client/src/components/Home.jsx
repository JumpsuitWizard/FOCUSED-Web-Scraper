import React, { useState, useEffect } from "react";
import Tab from "./Tab";
import Companies from "./Companies";
import CompanyDetails from "./CompanyDetails";

const Home = ({ data }) => {
  const [selectedTab, setSelectedTab] = useState("Companies");
  const [companyName, setCompanyName] = useState("");

  const handleTabSelect = (title) => {
    setSelectedTab(title);
  };

  const handleCompanyName = (name) => {
    setCompanyName(name);
  };

  return (
    <>
      <div className="ml-20">
        {!companyName && (
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
        )}
        {selectedTab === "Companies" && !companyName && (
          <Companies data={data} handleCompanyName={handleCompanyName} />
        )}
      </div>
      {companyName && <CompanyDetails companyName={companyName} />}
    </>
  );
};

export default Home;
