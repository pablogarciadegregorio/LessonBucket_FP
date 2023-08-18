import React, { useState } from "react";
import { Link } from "react-router-dom";



export const Sidebar = () => {

    const [showSidebar, setShowSidebar] = useState("spread")
    console.log(showSidebar)

   const  handleToggleSideBar = () => {

        if (showSidebar === "spread") {setShowSidebar("shrink")}
        else {setShowSidebar("spread")}
    }




    if (showSidebar === "spread") {
        
        return (
        <>
            
                < nav className="sidebar mt-5 align-items-center my-auto py-4 pe-5 ps-3 ">

            <ul className="list-unstyled components mb-0 pb-0">
                <li>
                    <i className=" arrow-left fa-solid fa-arrow-left ms-3 me-3  mb-3 d-flex justify-content-end" onClick={handleToggleSideBar}></i>
                    
                </li>
                <li className="pt-0 dashboard">
                <i className="fa-solid fa-table-cells-large m-3 "></i>
                <a className="">Dashboard</a>

                </li>
                <li className="students">
                    <i className="fa-solid fa-graduation-cap m-3"></i>
                    <a className="">Students</a>
                </li>
                <li className="subjects">
                    <i className="fa-solid fa-book m-3"></i>
                    <a className="">Subjects</a>

                </li>
                <li className="profile">
                    <i className="fa-solid fa-user m-3"></i>
                    <a className="">Profile</a>
                </li>
                <li className="settings">
                   <i className="fa-solid fa-gear m-3 "></i>
                   <a className="">Settings</a>
                </li>
                <li className="documents">
                    <i class="fa-regular fa-folder-open m-3"></i>
                    <a className="">Documents</a>
                </li>
            </ul>

        </nav >

        
    </>

    );}

    else {
        return (
        <>
            
                < nav className="sidebar mt-5 align-items-center my-auto py-4 pe-2 ps-3 ">

            <ul className="list-unstyled components mb-0 pb-0">
                <li>
                <i className="arrow-right fa-solid fa-arrow-right ms-3 me-3  mb-3" onClick={handleToggleSideBar}></i>
                    
                </li>
                <li className="pt-0 dashboard">
                <i className="fa-solid fa-table-cells-large m-3 "></i>
                

                </li>
                <li className="students">
                    <i className="fa-solid fa-graduation-cap m-3"></i>
                    
                </li>
                <li className="subjects">
                    <i className="fa-solid fa-book m-3"></i>
                    

                </li>
                <li className="profile">
                    <i className="fa-solid fa-user m-3"></i>
                    
                </li>
                <li className="settings">
                   <i className="fa-solid fa-gear m-3 "></i>
                   
                </li>
                <li className="documents">
                    <i class="fa-regular fa-folder-open m-3"></i>
                  
                </li>
            </ul>

        </nav >

        
    </>

    );
    }

    

    
};