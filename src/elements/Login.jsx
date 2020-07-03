import React, {useState ,useEffect } from 'react';
import NavBar from '../container/NavBar';
// import Footer from '../container/Footer';
import './login.css';
import { Link  ,useHistory} from 'react-router-dom';
import { connect } from "react-redux";
import {authLogin} from '../store/action/loginAuth'

function Login(props) {
    
    const [email,setemail] = useState('');
    const [password,setpassword] = useState('');
    const [test , setTest] = useState(false);
    let history = useHistory();

    
    const redirect = () => {
        const token = localStorage.getItem('access')
        if (token) {
            history.push('/')
        }   
    }
    
    useEffect(() => {
        redirect()
    },[props]);
    
    const handleSubmit = e => {
        e.preventDefault();
        console.log("-sadas-asdas-das-d-a-sd-a-s-ad")
        console.log(props)
        // setTest(!test);
        if (email ==='' || password === '') {
            if (test === false){
                setTest(!test)
            }
        }
        else{      
            props.login(email,password)
            if (test === true){
                setTest(!test)
            }
        }
    };


    return(
        <div>
        {redirect}
        <div>
            <NavBar />
        </div>
        
        <div class ="loginform" onSubmit ={handleSubmit}>            
            <form>
                <div class="form-group">
                    <label for="formGroupExampleInput">Email</label>
                    <input type="email" class="form-control" id="formGroupExampleInput" 
                    value = {email}
                    onChange={(e)=>{setemail(e.target.value)}}
                    placeholder="Email" />
                 </div>
                <div class="form-group">
                    <label for="formGroupExampleInput2">Password</label>
                    <input type="password" class="form-control" id="formGroupExampleInput2" 
                    value = {password}
                    onChange={(e) => setpassword(e.target.value)}
                    placeholder="Password" />
                </div>
                <div>
                <button type="submit" 
                class="btn btn-outline-warning">
                    Login
                </button> 
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <Link>Sign Up</Link>
                </div>
                {test?<p>Please Try Again</p>:<p></p> }
            </form>
        </div>
{/*         
        <div class = "footer">
            <Footer/>
        </div>
         */}
        </div>

    )
}

const mapStateToProps = state => {
    return {
        loading : state.loading,
        error : state.error,
        token : state.token
    };
}

const mapDispatchToProps =  dispatch => {
    return {
    login : (username,password) => dispatch(authLogin(username,password))       
    };
}
export default connect(
    mapStateToProps,
    mapDispatchToProps
  )(Login);