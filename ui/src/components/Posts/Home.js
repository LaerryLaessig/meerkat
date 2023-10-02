import axios from "axios";
import { useEffect, useState } from "react";
import PostItem from "./PostItem";


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
          {posts.map(p => {
            return (<PostItem key={p.id} post={p}></PostItem>)
          })}
        </div>
      </div >
    </>
  );
}

export default Home;