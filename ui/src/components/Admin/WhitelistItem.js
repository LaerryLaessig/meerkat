function WhiteListItem(e) {
    return (
        <>
            <div className="card">
                <div className="card-body">
                    <h2 className="card-title h5">{e.item.email}</h2>
                </div>
                <div className="d-grid">
                    <button className="btn btn-outline-danger">
                        Delete
                    </button>
                </div>
            </div>
        </>
    )
}

export default WhiteListItem;