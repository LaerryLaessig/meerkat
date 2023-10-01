import axios from "axios";
import { useEffect, useState } from "react";

function Post(p) {
  return (
    <>
      <span key={p.id} className="author-right">created by {p.post.creator}</span>
      <div key={p.id} className="card" style={{ "display": "inline.flex" }}>
        <form method="POST" style={{ "paddingRight": "1em" }}>
          <div className="card-body">
            <h2 className="card-title h5">{p.post.title}</h2>
            <span className="card-text" style={{ "whiteSpace": "pre-line" }}>{p.post.text}</span>
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
  )
}


function Home(props) {

  const [posts, setPosts] = useState([]);
  useEffect(() => {
    axios({
      method: "GET",
      url: "/api/post",
      headers: {
        Authorization: 'Bearer ' + props.token
      }
    })
      .then((response) => {
        const res = response.data
        res.access_token && props.setToken(res.access_token)
        setPosts(res)
      }).catch((error) => {
        console.log(error.response)
      })
  }, [props]);


  return (
    <>
      <div className="signin-inner my-4 my-lg-0 bg-white shadow-soft border rounded border-gray-300 p-4 p-lg-5 w-100 fmxw-500">
        <h1 className="h4">Home</h1>
        <div className="d-grid" style={{ "paddingBottom": "1em" }}>
          <a href="/" className="btn btn-outline-info" role="button">Create Post</a>
        </div>
        <div className="col-md">
          {posts.length > 0 ?
            <>
              {posts.map(p => {
                return (<Post key={p.id} post={p}></Post>)
              })}
            </> : <></>}
        </div>
      </div >
    </>
  );
}

export default Home;