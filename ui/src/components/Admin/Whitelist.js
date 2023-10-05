import axios from "axios";
import { useCallback, useEffect, useState } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faEnvelope } from '@fortawesome/free-solid-svg-icons'


function Whitelist(props) {

  const get_new_whitelist = useCallback(() => {
    axios({
      method: "GET",
      url: "/api/whitelist",
      headers: {
        Authorization: 'Bearer ' + props.token
      }
    })
      .then((response) => {
        const res = response.data
        res.access_token && props.setToken(res.access_token)
        setWhitelist(prevNote => ({
          ...prevNote, items: res
        }))
      }).catch((error) => {
        console.log(error.response)
      })
  }, [props]);

  function WhiteListItem(e) {
    function deleteWhitelistItem(event) {
      axios({
        method: "DELETE",
        url: "/api/whitelist/" + e.item.id,
        headers: {
          Authorization: 'Bearer ' + props.token
        }
      }).then(() => {
        get_new_whitelist()
      })
        .catch((error) => {
          if (error.response) {
            console.log(error.response)
            console.log(error.response.status)
            console.log(error.response.headers)
          }
        })
    }

    return (
      <>
        <div className="card">
          <div className="card-body">
            <h2 className="card-title h5">{e.item.email}</h2>
          </div>
          <div className="d-grid">
            <button onChange={handleChange} onClick={deleteWhitelistItem} className="btn btn-outline-danger">
              Delete
            </button>
          </div>
        </div>
      </>
    )
  }

  const [whitelist, setWhitelist] = useState({
    items: [],
    new_email: ""
  });



  useEffect(() => {
    get_new_whitelist()
  }, [props, get_new_whitelist]);

  function addWhiteListItem(event) {
    axios({
      method: "POST",
      url: "/api/whitelist",
      headers: {
        Authorization: 'Bearer ' + props.token
      },
      data: {
        email: whitelist.new_email,
      }
    })
      .catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
        }
      })
  }

  function handleChange(event) {
    const { value, name } = event.target
    setWhitelist(prevNote => ({
      ...prevNote, [name]: value
    })
    )
    event.preventDefault()
  }

  return (
    <>
      <div className="signin-inner my-4 my-lg-0 bg-white shadow-soft border rounded border-gray-300 p-4 p-lg-5 w-100 fmxw-500">
        <h1 className="h4">Whitelist</h1>
        <form>
          <div className="form-group">
            <div className="form-group mb-4">
              <label className="form-control-label">E-Mail</label>
              <div className="input-group">
                <span className="input-group-text"><FontAwesomeIcon icon={faEnvelope} /></span>
                <input
                  onChange={handleChange}
                  className="form-control form-control-lg"
                  placeholder="example@gmail.com"
                  text={whitelist.new_email}
                  name="new_email"
                  value={whitelist.new_email} />
              </div>
              <div className="d-grid">
                <button className="btn btn-outline-primary" onClick={addWhiteListItem}>Save</button>
              </div>
            </div>
          </div>
        </form>
        {whitelist.items.map(w => {
          return <WhiteListItem key={w.id} item={w} />
        })}
      </div>
    </>
  );
}

export default Whitelist;