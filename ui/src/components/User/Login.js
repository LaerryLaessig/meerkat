import { useState } from 'react';
import axios from "axios";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUnlockAlt, faEnvelope } from '@fortawesome/free-solid-svg-icons'

function Login(props) {

  const [loginForm, setloginForm] = useState({
    email: "",
    password: ""
  })

  function login(event) {
    axios({
      method: "POST",
      url: "/login",
      data: {
        email: loginForm.email,
        password: loginForm.password
      }
    })
      .then((response) => {
        props.setToken(response.data.access_token)
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
        }
      })

    setloginForm(({
      email: "",
      password: ""
    }))

    event.preventDefault()
  }

  function handleChange(event) {
    const { value, name } = event.target
    setloginForm(prevNote => ({
      ...prevNote, [name]: value
    })
    )
  }

  return (
    <>
      <div className="signin-inner my-4 my-lg-0 bg-white shadow-soft border rounded border-gray-300 p-4 p-lg-5 w-100 fmxw-500">
        <div className="text-center text-md-center mb-4 mt-md-0">
          <h1 className="mb-0 h4">Log in</h1>
        </div>
        <form className="mt-4">
          <div className="form-group mb-4">
            <label className="form-control-label">E-Mail</label>
            <div className="input-group">
              <span className="input-group-text"><FontAwesomeIcon icon={faEnvelope} /></span>
              <input onChange={handleChange}
                className="form-control form-control-lg"
                type="email"
                text={loginForm.email}
                name="email"
                autoComplete="email"
                placeholder="example@mail.com"
                value={loginForm.email} />
            </div>
          </div>
          <div className="form-group">
            <div className="form-group mb-4">
              <label className="form-control-label">Password</label>
              <div className="input-group">
                <span className="input-group-text"><FontAwesomeIcon icon={faUnlockAlt} /></span>
                <input onChange={handleChange}
                  className="form-control form-control-lg"
                  type="password"
                  text={loginForm.password}
                  name="password"
                  autoComplete="current-password"
                  placeholder="Password"
                  value={loginForm.password} />
              </div>
            </div>
            <div className="d-flex justify-content-between align-items-center mb-4">
              <div><a href="/forgotpassword">Forgot password</a></div>
            </div>
          </div>
          <div className="btn-group">
            <button className="btn btn-outline-primary" onClick={login}>Sign In</button>
          </div>
        </form>
        <div className="d-flex justify-content-center align-items-center mt-4">
          <span className="fw-normal">
            Not registered?
            Sign up <a href="/register">here</a>!
          </span>
        </div>
      </div >
    </>
  );
}

export default Login;