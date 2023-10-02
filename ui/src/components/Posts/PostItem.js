function PostItem(p) {
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

export default PostItem;