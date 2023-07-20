import React, { useState } from "react";

const Companies = () => {
  // Sample list of companies, you can replace this with your actual data
  const companiesList = [
    { id: 1, name: "Company A" },
    { id: 2, name: "Company B" },
    { id: 3, name: "Company C" },
    { id: 4, name: "Company D" },
    { id: 5, name: "Company E" },
    { id: 6, name: "Company F" },
    { id: 7, name: "Company G" },
    { id: 8, name: "Company H" },
    { id: 9, name: "Company I" },
    { id: 10, name: "Company J" },
    { id: 11, name: "Company K" },
    { id: 12, name: "Company L" },
    { id: 13, name: "Company M" },
    { id: 14, name: "Company N" },
    // Add more companies as needed
  ];

  const itemsPerPage = 6; // Number of items to show per page
  const [currentPage, setCurrentPage] = useState(1);

  // Function to slice the companies list based on the current page
  const paginateCompanies = (companies) => {
    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    return companies.slice(startIndex, endIndex);
  };

  // Function to handle previous page click
  const handlePrevPage = () => {
    setCurrentPage((prevPage) => Math.max(prevPage - 1, 1));
  };

  // Function to handle next page click
  const handleNextPage = () => {
    setCurrentPage((prevPage) =>
      Math.min(prevPage + 1, Math.ceil(companiesList.length / itemsPerPage))
    );
  };

  const paginatedCompanies = paginateCompanies(companiesList);

  return (
    <div className="mt-14 grid grid-cols-3 gap-4 gap-y-12">
      {paginatedCompanies.map((company) => (
        <div key={company.id} className="w-96 h-80 bg-zinc-100 rounded-lg p-6">
          <div className="w-96 h-10 text-black text-xl font-bold">
            Company Name
          </div>
          <div className="w-96 h-10 text-black text-xl font-bold">
            Dependencies
          </div>
          <div className="inline-flex gap-2 flex-wrap">
            <Badges text="Python" />
            <Badges text="Java" />
            <Badges text="JavaScript" />
            <Badges text="React" />
            <Badges text="Node.js" />
            <Badges text="Docker" />
            <Badges text="AWS" />
            <Badges text="PostgreSQL" />
            <Badges text="React" />
            <Badges text="Node.js" />
            <Badges text="Docker" />
            <Badges text="React" />
            <Badges text="Node.js" />
            <Badges text="Docker" />
          </div>
        </div>
      ))}
      <div className="col-span-3 flex justify-center mt-4">
        <button
          className="px-4 py-2 bg-blue-600 text-white rounded-md mr-2"
          onClick={handlePrevPage}
          disabled={currentPage === 1}
        >
          Previous
        </button>
        <button
          className="px-4 py-2 bg-blue-600 text-white rounded-md"
          onClick={handleNextPage}
          disabled={
            currentPage >= Math.ceil(companiesList.length / itemsPerPage)
          }
        >
          Next
        </button>
      </div>
    </div>
  );
};

export const Badges = ({ text }) => {
  return (
    <div className="w-auto h-9 rounded-lg border border-neutral-400 px-2 py-1">
      <div className="text-blue-950 text-base font-medium">{text}</div>
    </div>
  );
};

export default Companies;
