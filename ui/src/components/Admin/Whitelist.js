import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faEnvelope } from '@fortawesome/free-solid-svg-icons'

function WhiteListItem() {
  return (
    <>
      <div className="card">
        <div className="card-body">
          <h2 className="card-title h5">email</h2>
        </div>
        <div className="d-grid">
          <form method="POST">
            <button className="btn btn-outline-danger"
              formaction="">
              Delete
            </button>
          </form>
        </div>
      </div>
    </>
  )
}


function Whitelist(props) {
  return (
    <>
      <div className="signin-inner my-4 my-lg-0 bg-white shadow-soft border rounded border-gray-300 p-4 p-lg-5 w-100 fmxw-500">
        <h1 className="h4">Whitelist</h1>
        <form method="post" action="">
          <fieldset className="form-group">
            <div className="form-group">
              <div className="form-group mb-4">
                <label className="form-control-label">E-Mail</label>
                <div className="input-group">
                  <span className="input-group-text"><FontAwesomeIcon icon={faEnvelope} /></span>
                  <input className="form-control form-control-lg" placeholder="example@gmail.com"></input>
                </div>
                <div className="d-grid">
                  <button className="btn btn-outline-primary">Save</button>
                </div>
              </div>
            </div>
          </fieldset>
        </form>
      </div>
    </>
  );
}

export default Whitelist;