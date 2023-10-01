function Post() {
  return (
    <>
      <span className="author-right ">created by creator</span>
      <div className="card" style="display: inline.flex;">
        <form method="POST" style={{ "paddingRight": "1em" }}>
          <div className="card-body">
            <h2 className="card-title h5">Title</h2>
            <span className="card-text" style={{ "whiteSpace": "pre-line" }}>text</span>
          </div>
        </form>
        <div className="btn-group" role="group">
          <form method="GET">
            <button className="btn btn-outline-success" formaction="">
              Edit
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


function Home(props) {

  return (
    <>
      <div className="signin-inner my-4 my-lg-0 bg-white shadow-soft border rounded border-gray-300 p-4 p-lg-5 w-100 fmxw-500">
        <h1 className="h4">Home</h1>
        <div className="d-grid" style={{ "paddingBottom": "1em" }}>
          <a href="" className="btn btn-outline-info" role="button">Create Post</a>
        </div>
        <div className="col-md">

        </div>
      </div>
    </>
  );
}

export default Home;