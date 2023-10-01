import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAddressCard, faEnvelope } from '@fortawesome/free-solid-svg-icons'

function Account(props) {

  return (
    <>
      <div className="signin-inner my-4 my-lg-0 bg-white shadow-soft border rounded border-gray-300 p-4 p-lg-5 w-100 fmxw-500">
        <h1 className="mb-0 h4">Account data</h1>
        <form method="POST" action="">
          <fieldset className="form-group">

            <div className="form-group mb-4">
              <label className="form-control-label">Username</label>
              <div className="input-group">
                <span className="input-group-text"><FontAwesomeIcon icon={faAddressCard} /></span>
                <input type="text" className="form-control form-control-lg"></input>
              </div>
            </div>
            <div className="form-group">
              <label className="form-control-label">E-Mail</label>
              <div className="input-group">
                <span className="input-group-text"><FontAwesomeIcon icon={faEnvelope} /></span>
                <input type="text" className="form-control form-control-lg"></input>
              </div>
            </div>
          </fieldset>
          <div className="btn-group">
            <button className="btn btn-outline-info">save</button>
          </div>
        </form>
      </div >
    </>

  );
}

export default Account;