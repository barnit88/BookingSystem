import * as actionTypes from './actionType';
import axios from 'axios';



export const authStart = () => {
    return{
        type: actionTypes.AUTH_START
    }
}

export const authSuccess = token => {
    return {
        type : actionTypes.AUTH_SUCCESS,
        token : token
    }
}

export const authFail = error => {
    return {
        type : actionTypes.AUTH_FAIL ,
        error : error
    }
}


export const authLogin = (username , password) => {
    return dispatch => {
        dispatch(authStart());
        // console.log("yeasada")
        // console.log(username,password)
        axios.post('http://127.0.0.1:8000/api/account/login/',
        {
            email       : username,
            password    : password
        })
        .then(res => {
            console.log('From Utha');
            console.log(res);
            console.log(res.data.access);
            console.log(res.data.refresh);
            console.log("--------------");
            
            const access = res.data.access;
            const refresh = res.data.refresh;
            localStorage.setItem('access', access);
            localStorage.setItem('refresh', refresh);
            const token = res.data.access;
            dispatch(authSuccess(token));
        })
        .catch(err => {
            // console.log(err);
            dispatch(authFail(err));
            
        })

    }
}