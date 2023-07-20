import React, { useState, useEffect } from "react";
import { Badges } from "./Companies";

const CompanyDetails = ({ companyName }) => {
  const [companyData, setCompanyData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:4000/dependencies/company/${companyName}`
        );
        const data = await response.json();

        const transformedData = data.components;

        // Sort the array based on the number of shared_authors in descending order
        transformedData.sort(
          (a, b) => b.shared_authors.length - a.shared_authors.length
        );

        setCompanyData(transformedData);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);
  return (
    <div className="flex flex-col items-center">
      <div className="text-black text-3xl pb-5">
        {companyName.toLowerCase().replace(/\b\w/g, (l) => l.toUpperCase())}
      </div>
      {/* <div className="w-96 h-10 text-black text-2xl font-bold">
        Dependencies
      </div> */}
      <table className="divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th
              scope="col"
              className="px-6 py-3 text-left font-medium text-gray-500 uppercase tracking-wider"
            >
              Dependency
            </th>
            <th
              scope="col"
              className="px-6 py-3 text-left font-medium text-gray-500 uppercase tracking-wider"
            >
              Companies sharing the dependency
            </th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {companyData &&
            companyData.map((value, i) => (
              <tr key={i}>
                <td className="px-6 py-4 whitespace-nowrap">
                  <Badges text={value.name} />
                </td>
                {value.shared_authors.length > 0 ? (
                  <td className="px-6 py-4 flex space-x-5 whitespace-nowrap">
                    {value.shared_authors.map((val, index) => (
                      <Badges
                        key={index}
                        text={val.replace(/\b\w/g, (l) => l.toUpperCase())}
                      />
                    ))}
                  </td>
                ) : (
                  <td className="px-6 py-4 whitespace-nowrap text-gray-500">
                    No shared authors
                  </td>
                )}
              </tr>
            ))}
        </tbody>
      </table>
    </div>
  );
};

export default CompanyDetails;
