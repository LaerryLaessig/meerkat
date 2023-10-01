import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAddressCard, faEnvelope, faUnlockAlt } from '@fortawesome/free-solid-svg-icons'

function Register(props) {

  return (
    <>
      <div className="signin-inner my-4 my-lg-0 bg-white shadow-soft border rounded border-gray-300 p-4 p-lg-5 w-100 fmxw-500">
        <div className="text-center text-md-center mb-4 mt-md-0">
          <h1 className="mb-0 h4">Register</h1>
        </div>
        <form>
          <div className="form-group mb-4">
            <label className="form-control-label">Username</label>
            <div className="input-group">
              <span className="input-group-text"><FontAwesomeIcon icon={faAddressCard} /></span>
              <input type="text" className="form-control form-control-lg" placeholder="Username"></input>
            </div>
          </div>
          <div className="form-group mb-4">
            <label className="form-control-label">E-Mail</label>
            <div className="input-group">
              <span className="input-group-text"><FontAwesomeIcon icon={faEnvelope} /></span>
              <input type="text" className="form-control form-control-lg" placeholder="example@mail.com"></input>
            </div>
          </div>
          <div className="form-group">
            <div className="form-group mb-4">
              <label className="form-control-label">Password</label>
              <div className="input-group">
                <span className="input-group-text"><FontAwesomeIcon icon={faUnlockAlt} /></span>
                <input type="password" className="form-control form-control-lg" placeholder="Password"></input>
              </div>
            </div>
            <div className="form-group mb-4">
              <label className="form-control-label">Confirm Password</label>
              <div className="input-group">
                <span className="input-group-text"><FontAwesomeIcon icon={faUnlockAlt} /></span>
                <input type="password" className="form-control form-control-lg" placeholder="Confirm Password"></input>
              </div>
            </div>
          </div>
          <div className="btn-group">
            <button className="btn btn-outline-primary">Sign Up</button>
          </div>
        </form>
        <div className="d-flex justify-content-center align-items-center mt-4">
          <span className="text-muted">
            Already have an account?
            Sign in <a href="/login">here</a>!
          </span>
        </div>
      </div>
    </>
  );
}

export default Register;