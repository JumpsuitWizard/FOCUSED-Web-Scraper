import React, { useState, useEffect } from "react";
import { Badges } from "./Companies";
import { Link, useParams } from "react-router-dom";
import Loader from "./Loader";

const CompanyDetails = () => {
  const [companyData, setCompanyData] = useState(null);
  const { companyName } = useParams();
  const [uniqueAuthors, setUniqueAuthors] = useState();
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedAuthors, setSelectedAuthors] = useState([]);
  const [filteredCompanyData, setFilteredCompanyData] = useState([]);
  const [strictOption, setstrictOption] = useState(false);
  const handleOptionChange = () => {
    setstrictOption(!strictOption);
  };

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

        const uniqueAuthors = new Set(
          transformedData.flatMap((item) => item.shared_authors)
        );

        setUniqueAuthors([...uniqueAuthors]);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, [companyName]);

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
  };

  const filteredAuthors =
    uniqueAuthors &&
    uniqueAuthors.filter((author) =>
      author.toLowerCase().includes(searchTerm.toLowerCase())
    );

  const handleCheckboxChange = (author) => {
    setSelectedAuthors((prevSelected) => {
      if (prevSelected.includes(author)) {
        return prevSelected.filter((selected) => selected !== author);
      } else {
        return [...prevSelected, author];
      }
    });
  };

  useEffect(() => {
    if (companyData) {
      if (selectedAuthors.length === 0) {
        setFilteredCompanyData(companyData);
      } else {
        if (strictOption) {
          setFilteredCompanyData(
            companyData.filter((data) =>
              selectedAuthors.every((author) =>
                data.shared_authors.includes(author)
              )
            )
          );
        } else {
          setFilteredCompanyData(
            companyData.filter((data) =>
              data.shared_authors.some((author) =>
                selectedAuthors.includes(author)
              )
            )
          );
        }
      }
    }
  }, [companyData, selectedAuthors, strictOption]);

  if (companyData === null) {
    return <Loader />;
  }

  return (
    <div className="bg-zinc-100 h-screen w-screen flex flex-col items-center">
      <div className="text-black text-3xl pb-5 pt-8">
        {companyName.toLowerCase().replace(/\b\w/g, (l) => l.toUpperCase())}
      </div>
      <div className="flex justify-evenly">
        <div className="w-64 bg-gray-200 rounded-lg pt-3 flex flex-col items-center">
          <div className="text-black text-base font-normal mb-2">Filter By</div>
          <input
            className=" rounded-3xl pl-3 pr-3 py-1 text-black text-1xl font-normal bg-white"
            type="text"
            placeholder="Search"
            value={searchTerm}
            onChange={handleSearch}
          />
          <div className="flex items-center mt-3 ml-8">
            <input
              type="checkbox"
              id="checkbox-strict"
              checked={strictOption}
              className="form-checkbox h-5 w-5 text-cyan-600 rounded focus:ring-cyan-400 focus:ring-offset-0"
              onChange={handleOptionChange}
            />
            <label htmlFor="checkbox-strict" className="ml-2 text-gray-700">
              Only show shared dependencies
            </label>
          </div>

          <div className=" ml-5 mt-4 grid grid-cols-2 gap-4">
            {filteredAuthors &&
              filteredAuthors.map((value, index) => (
                <div className="flex items-center" key={index}>
                  <input
                    type="checkbox"
                    id={`checkbox-${index}`}
                    className="form-checkbox h-5 w-5 text-cyan-600 rounded focus:ring-cyan-400 focus:ring-offset-0"
                    checked={selectedAuthors.includes(value)}
                    onChange={() => handleCheckboxChange(value)}
                  />
                  <label
                    htmlFor={`checkbox-${index}`}
                    className="ml-2 text-gray-700"
                  >
                    {value
                      .toLowerCase()
                      .replace(/\b\w/g, (l) => l.toUpperCase())}
                  </label>
                </div>
              ))}
          </div>
        </div>
        <div className="h-110 overflow-y-auto">
          <table className="table-auto border-collapse">
            <thead className="bg-cyan-600 bg-opacity-50 sticky top-0">
              <tr>
                <th className="px-6 py-3 text-left font-medium text-black uppercase tracking-wider w-4">
                  Dependency
                </th>
                <th className="px-6 py-3 text-left font-medium text-black uppercase tracking-wider">
                  Companies sharing the dependency
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {filteredCompanyData.map((value, i) => (
                <tr key={i}>
                  <td className="px-6 py-4 min-w-min border-r-4 border-gray-600">
                    <Badges text={value.name} type="package" />
                  </td>
                  {value.shared_authors.length > 0 ? (
                    <td className="px-6 py-4 flex space-x-5">
                      {value.shared_authors.map((val, index) => (
                        <Badges
                          key={index}
                          text={val.replace(/\b\w/g, (l) => l.toUpperCase())}
                          type="company"
                          highlight={selectedAuthors.includes(val)}
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
      </div>
      <div className="flex">
        <Link
          to="/"
          className="mt-5 w-96 h-14 mr-3 bg-cyan-600 bg-opacity-30 rounded-tl-lg rounded-lg cursor-pointer flex items-center justify-center font-semibold"
        >
          Go to Home
        </Link>
        <Link
          to="/dashboard"
          className="mt-5 w-96 h-14 ml-3  bg-cyan-600 bg-opacity-30 rounded-tl-lg rounded-lg cursor-pointer flex items-center justify-center font-semibold"
        >
          Go to Dashboard
        </Link>
      </div>
    </div>
  );
};

export default CompanyDetails;
