import { NavLink } from "react-router-dom";

const Navbar = ({ searchTerm, handleSearch }) => {
  return (
    <div className="w-full h-24 bg-cyan-900 relative flex items-center">
      <div className="ml-5 text-white text-4xl font-normal">FOCUSED</div>

      <NavLink
        to="/"
        className="ml-52 text-white text-2xl font-normal hover:cursor-pointer relative"
      >
        {({ isActive }) => (
          <>
            HOME
            <span
              className={
                isActive ? "absolute -bottom-1 left-0 w-full h-1 bg-white" : ""
              }
            />
          </>
        )}
      </NavLink>

      <NavLink
        to="/dashboard"
        className="ml-10 text-white text-2xl font-normal hover:cursor-pointer relative"
      >
        {({ isActive }) => (
          <>
            DASHBOARD
            <span
              className={
                isActive ? "absolute -bottom-1 left-0 w-full h-1 bg-white" : ""
              }
            />
          </>
        )}
      </NavLink>

      <div className="right-5 absolute">
        <input
          className="w-64 h-11 rounded-3xl pl-5 pr-5 py-2 text-black text-1xl font-normal bg-white"
          type="text"
          placeholder="Search"
          value={searchTerm}
          onChange={handleSearch}
        />
      </div>
    </div>
  );
};

export default Navbar;
