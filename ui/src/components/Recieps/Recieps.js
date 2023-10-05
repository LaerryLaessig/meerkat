import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch } from '@fortawesome/free-solid-svg-icons'


function Reciep() {
  return (
    <>
      <span className="author-right ">created by creator</span>
      <div className="card" style={{ "display": "inline.flex" }}>
        <form method="POST">
          <div className="card-body">
            <h5 className="card-title">Title</h5>
            <ul className="list-group list-group-flush">
              <li className="list-group-item">
                <div className="input-group-text" style={{ "whiteSpace": "pre-wrap", "textAlign": "left" }}>
                  <span className="fas fa-shopping-basket icon-label"> amount ingredientname</span>
                </div>
              </li>
            </ul>
          </div>
        </form>
        <div className="btn-group" role="group">
          <form method="GET">
            <button className="btn btn-outline-success" formaction="">
              Edit
            </button>
          </form>
          <form method="POST">
            <button className="btn btn-outline-warning" formaction="">
              Generate Task
            </button>
          </form>
          <form method="POST">
            <button className="btn btn-outline-danger" formaction="">
              Delete
            </button>
          </form>
        </div>
      </div>
    </>
  )
}

function Recieps(props) {

  return (
    <>
      <div className="signin-inner my-4 my-lg-0 bg-white shadow-soft border rounded border-gray-300 p-4 p-lg-5 w-100 fmxw-500">
        <h1 className="h4">Recipes</h1>
        <div className="d-grid">

        </div>
        <div className="col-md">
          <div className="card-body">
            <form>
              <div className="form-group">
                <label className="form-control-label">Searchstring</label>
                <div className="input-group">
                  <span className="input-group-text"><FontAwesomeIcon icon={faSearch} /></span>
                  <input type="text" className="form-control form-control-lg"></input>
                </div>
              </div>
              <div className="btn-group" role="group">
                <button className="btn btn-outline-info">Search</button> <a href="/" className="btn btn-outline-success" role="button">Create New Recipe</a>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  );
}

export default Recieps;