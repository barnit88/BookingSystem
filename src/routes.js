import React from 'react';
import { Route } from 'react-router-dom';
import StartingLayout from './container/Layout'
import Login from './elements/Login'
// import ArticleList from './containers/ArticleListView';
// import ArticleDetail from './containers/ArticleDetailView';
// import LoginForm from './containers/Login';
// import Signup from './containers/Login';
// import RegistrationForm from './containers/Signup';



const BaseRouter = () => (
    <div>
        <Route exact path = '/' component = {StartingLayout}/>
        {/* <Route exact path = '/articles/:articleID/' component = {ArticleDetail}/> */}
        <Route exact path = '/login/' component = {Login}/>
        {/* <Route exact path = '/signup/' component = {RegistrationForm}/> */}
    </div>    
);

export default BaseRouter;
