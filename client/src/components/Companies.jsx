import React from "react";
import { FaArrowRightLong } from "react-icons/fa6";

const Companies = ({ data, handleCompanyName }) => {
  return (
    <div className="mt-14 grid grid-cols-3 gap-4 gap-y-12">
      {data.map((company) => (
        <div
          key={company.index}
          className="w-96 h-80 bg-zinc-100 rounded-lg p-6 relative"
        >
          <div className="w-96 h-10 text-black text-xl font-bold">
            {company.company_name
              .toLowerCase()
              .replace(/\b\w/g, (l) => l.toUpperCase())}
          </div>
          <div className="w-96 h-10 text-black text-xl font-bold">
            Dependencies
          </div>
          <div
            className="flex gap-2 flex-wrap"
            style={{ maxHeight: "11rem", overflowY: "auto" }}
          >
            {[...new Set(company.packages)].map((value) => (
              <Badges key={value} text={value.toLowerCase()} />
            ))}
          </div>
          <button
            type="button"
            onClick={() => handleCompanyName(company.company_name)}
            className="absolute bottom-3 right-6 cursor-pointer"
          >
            <FaArrowRightLong size={24} />
          </button>
        </div>
      ))}
    </div>
  );
};

export const Badges = ({ text }) => {
  return (
    <div className="inline-block h-9 rounded-lg border border-neutral-400 px-2 py-1">
      <div className="text-blue-950 text-base font-medium">{text}</div>
    </div>
  );
};

export default Companies;
