function SubtaskItem(e) {
    return (
        <>
            <li className="list-group-item">
                <div className="input-group-text" style={{ "whiteSpace": "pre-wrap" }}>
                    <span className="fas fa-check-circle" style={{ "word-wrap": "break-word" }}>
                        <s>{e.item.name}</s></span>
                </div>
            </li>
            <li className="list-group-item">
                <div className="input-group-text" style={{ "whiteSpace": "pre-wrap" }}>
                    <span className="fas fa-times-circle"> {e.item.name} </span>
                </div>
            </li>
        </>
    )
}

export default SubtaskItem;