import React, { useState, useEffect } from "react";
import DashboardChart from "./DashboardChart";
import VerticalChart from "./VerticalChart";
import Loader from "./Loader";

const Dashboard = () => {
  const [packageCountData, setPackageCountData] = useState(null);
  const [maxUniqueCount, setMaxUniqueCount] = useState(null);
  const [percentagePackage, setPercentagePackage] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:4000/dependencies/package/count`
        );
        const data = await response.json();

        const transformedData = data.components.slice(0, 10);
        setPackageCountData(transformedData);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();

    const fetchUniqueData = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:4000/dependencies/package/companies_with_max_unique_counts`
        );
        const data = await response.json();

        const transformedData = data.components.slice(0, 10);
        setMaxUniqueCount(transformedData);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchUniqueData();

    const fetchPercentage = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:4000/dependencies/package/package_percentage`
        );
        const data = await response.json();

        const transformedData = data.components.slice(0, 10);
        // Use map to modify the 'percentage' value for each element
        const roundedValueList = transformedData.map((val) => ({
          ...val,
          count: Math.floor(val.count), // Round down the percentage
        }));
        setPercentagePackage(roundedValueList);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchPercentage();
  }, []);
  if (packageCountData === null) {
    return <Loader />;
  }
  if (maxUniqueCount === null) {
    return <Loader />;
  }
  if (percentagePackage === null) {
    return <Loader />;
  }

  return (
    <div className="mt-14 flex flex-col items-center">
      <div className="flex">
        <div className="w-100 h-80 rounded-lg p-4 relative translate-z-10 shadow-md">
          <div className="w-100 h-12 text-black text-opacity-70 text-xl absolute top-0 left-0  bg-cyan-600 bg-opacity-50 rounded-t-lg flex items-center pl-4 text-center">
            Open Source Dependencies Count
          </div>
          <DashboardChart data={packageCountData} />
          <p className="text-gray-800 text-base font-normal">
            This chart shows the total number of occurrences of each dependency
            common between all the companies.
          </p>
        </div>
        <div className="w-100 h-80 ml-32 rounded-lg p-6 relative translate-z-10 shadow-md">
          <div className="w-100 h-12 text-black text-opacity-70 text-xl absolute top-0 left-0  bg-cyan-600 bg-opacity-50 rounded-t-lg flex items-center pl-4 text-center">
            Companies with Maximum Unique Dependencies
          </div>
          <DashboardChart data={maxUniqueCount} />
          <p className="text-gray-800 text-base font-normal">
            This chart shows the companies with maximum unique open source
            dependency.
          </p>
        </div>
      </div>
      <div className="w-110 h-96 mt-14 rounded-lg p-6 relative translate-z-10 shadow-md">
        <div className="w-110 h-12 text-black text-opacity-70 text-xl absolute top-0 left-0  bg-cyan-600 bg-opacity-50 rounded-t-lg flex items-center pl-4 text-center">
          Open Source Dependency Percentage
        </div>
        <VerticalChart data={percentagePackage} />
        <p className="text-gray-800 text-base font-normal pt-2">
          This chart shows the percentage of companies using a open source
          dependency.
        </p>
      </div>
    </div>
  );
};

export default Dashboard;
