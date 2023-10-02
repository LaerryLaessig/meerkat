import axios from "axios";

function WhiteListItem(e) {
    function deleteWhitelistItem(event) {
        axios({
            method: "DELETE",
            url: "/api/whitelist/" + e.item.id,
            headers: {
                Authorization: 'Bearer ' + e.token
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

    return (
        <>
            <div className="card">
                <div className="card-body">
                    <h2 className="card-title h5">{e.item.email}</h2>
                </div>
                <div className="d-grid">
                    <button onClick={deleteWhitelistItem} className="btn btn-outline-danger">
                        Delete
                    </button>
                </div>
            </div>
        </>
    )
}

export default WhiteListItem;