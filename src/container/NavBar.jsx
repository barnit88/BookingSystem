import React from "react";
import { Link } from 'react-router-dom';


function NavBar() {

    return (
        <nav class="navbar fixed-top navbar-dark bg-info d-flex flex-row-reverse">
            <ul class="nav nav-pills">
                <Link to ="/">
                    <li class="nav-item">
                        <a class="nav-link text-warning " href="#!">Active</a>
                    </li>
                </Link>
                <Link to ="/login">
                <li class="nav-item">
                    <a class="nav-link text-warning " href="#!">Login</a>
                </li>
                </Link>
                <Link>
                <li class="nav-item">
                    <a class="nav-link text-warning disabled" href="#!">Disabled</a>
                </li>
                </Link>
            </ul> 
        </nav>
    );
}

export default NavBar;