import React, { useContext} from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { BackendURL } from "./component/backendURL";
import { Home } from "./pages/home";
import { Login } from "./pages/login";
import { TermsAndConditions } from "./pages/termsAndConditions";
import { RecoverPass } from "./pages/recoverPass";
import { Students } from "./pages/students";
import { Donations } from "./pages/donations";
import { Single } from "./pages/single";
import { SubjectsPage } from "./pages/subjectsPage";
import injectContext from "./store/appContext";
import { Navbar } from "./component/navbar/navbar";
import { Footer } from "./component/footer/footer";
import { Sidebar } from "./component/sidebar/sidebar";
import { Dashboard } from "./pages/dashboard"
import { Classes } from "./pages/classes"
import { Profile } from "./pages/Profile";
import { JobsNearby } from "./pages/JobsNearby"
import { Context } from "./store/appContext";



const Layout = () => {
   
    const basename = process.env.BASENAME || "";
    const { store, actions } = useContext(Context);


    if (!process.env.BACKEND_URL || process.env.BACKEND_URL == "") return <BackendURL />;



    return (
        <div>
            <BrowserRouter basename={basename}>
                <ScrollToTop>
                <Navbar />
                    <div className="container-fluid p-0">
                        <div className="row">
                            <div className={store.token === "" ? "col-2 p-0 d-none" : "col-1 p-0"}>
                            <Sidebar />                               
                            </div>
                       
                            <div className={store.token === "" ? "col-12 p-0" : "col-11 p-0"}>  
                            
                        <div className="min-vh-100 pt-4 mx-auto ">
                            <div className="mx-3">
                            <Routes>
                                <Route element={<Home />} path="/" />
                                <Route element={<Login />} path="/login" />
                                <Route element={<TermsAndConditions />} path="/termsAndConditions" />
                                <Route element={<RecoverPass />} path="/recoverPass" />
                                <Route element={<Students />} path="/students" />
                                <Route element={<Donations />} path="/donations" />
                                <Route element={<Dashboard />} path="/dashboard" />
                                <Route element={<Classes />} path="/classes" />
                                <Route element={<SubjectsPage />} path="/subjects" />
                                <Route element={<Single />} path="/single/:theid" />
                                <Route element={<Profile />} path="/profile" />
                                <Route element={<JobsNearby />} path="/jobsnearby" />
                                <Route element={<h1>Not found!</h1>} />
                            </Routes>
                            </div>
                            
                        </div>
                                                    
                            </div>
                         </div>
                    </div>
                    <Footer /> 
                </ScrollToTop>
            </BrowserRouter>
        </div>
    );
};

export default injectContext(Layout);