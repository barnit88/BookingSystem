import React from 'react';
import Sixth from '../Images/Sixth.jpg'
import './footer.css'

function Footer() {
    return(
            <div >
                <hr />
                <div class="container-fluid padding">
                    <div class= "row text-center">
                        <div class="col-md-4">
                            <img src ={Sixth} id="im" alt="it is"/>
                            <hr class="light" />
                            <p> 9842314388</p>
                            <p> barnit.basnet1@gmail.com</p>
                            <p> Itahari - Sunsari</p>
                        </div>
                        <div class= "col-md-4">
                            <hr class = "light" />
                            <h5> Our Hours</h5>
                            <hr class = "light" />
                            <p> Monday : 9am-5pm</p>
                            <p> Saturday : 10am : 2pm</p>
                            <p> Sunday : Closed</p>
                        </div> 
                        <div class= "col-md-4">
                            <hr class = "light" />
                            <h5> Our Hours</h5>
                            <hr class = "light" />
                            <p> city,State</p>
                            <p> city,State</p>
                            <p> city,State</p>
                            <p> Closed</p>
                        </div>   
                    </div>
                </div>
            </div>
    );
}



export default Footer;