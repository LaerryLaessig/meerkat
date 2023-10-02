

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