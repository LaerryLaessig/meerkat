function TaskItem(e) {
    return (
        <>
            <span className="author-right ">created by {e.item.creator}</span>
            <div className="card" style={{ "display": "inline.flex" }}>
                <form method="POST" style={{ "paddingRight": "1em" }}>
                    <div className="card-body">
                        <h5 className="card-title">{e.item.title}</h5>
                        <span className="input-group-text"><span className="fas fa-user-check"> {e.item.reviser}</span></span>
                        <ul className="list-group list-group-flush">
                            -- Subtasks
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

export default TaskItem;