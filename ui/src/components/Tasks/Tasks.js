
function TaskItem() {
  return (
    <>
      <span className="author-right ">created by creator</span>
      <div className="card" style={{ "display": "inline.flex" }}>
        <form method="POST" style={{ "paddingRight": "1em" }}>
          <div className="card-body">
            <h5 className="card-title">title</h5>
            <span className="input-group-text"><span className="fas fa-user-check"> reviser</span></span>
            <ul className="list-group list-group-flush">
              <li className="list-group-item">
                <div className="input-group-text" style={{ "whiteSpace": "pre-wrap" }}>
                  <span className="fas fa-check-circle" style={{ "word-wrap": "break-word" }}> <s>name</s></span>
                </div>
              </li>
              <li className="list-group-item">
                <div className="input-group-text" style={{ "whiteSpace": "pre-wrap" }}>
                  <span className="fas fa-times-circle"> name </span>
                </div>
              </li>
            </ul>
          </div>
        </form>
        <div className="btn-group" role="group">
          <form method="GET">
            <button className="btn btn-outline-success">
              Edit
            </button>
          </form>
          <form method="POST">
            <button className="btn btn-outline-danger">
              Delete
            </button>
          </form>
        </div>
      </div>
    </>
  );
}

function Tasks(props) {

  return (
    <>
      <div className="signin-inner my-4 my-lg-0 bg-white shadow-soft border rounded border-gray-300 p-4 p-lg-5 w-100 fmxw-500">
        <h1 className="h4">Tasks</h1>
        <div className="d-grid  btn-group" style={{ "paddingBottom": "1em" }}>
          <a href="/tasks" className="btn btn-outline-info" role="button">Create Task</a>
          <div className="dropdown">
            <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton"
              data-toggle="dropdown"
              aria-haspopup="true" aria-expanded="false">
              Filter
            </button>
            <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
              <a className="dropdown-item" href="tasks">Reviser</a>
              <a className="dropdown-item" href="tasks">Creator</a>
            </div>
          </div>
        </div>
        <div className="col-md">
        </div>
      </div>
    </>
  );
}

export default Tasks;