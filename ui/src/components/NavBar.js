import axios from "axios";
import AuthHandler from "../core/AuthHandler";

function NavBar(props) {
    const { hasJWT } = AuthHandler();

    function logout() {
        axios({
            method: "POST",
            url: "/api/logout",
            headers: {
                Authorization: 'Bearer '
            }
        })
            .then((response) => {
                props.token()
            }).catch((error) => {
                if (error.response) {
                    console.log(error.response)
                    console.log(error.response.status)
                    console.log(error.response.headers)
                }
            })
    }

    return (<>
        <ul className="nav nav-tabs justify-content-end">
            {hasJWT() ? <>
                <li className="nav-item"><a className="nav-link" href="/home">Home</a></li>
                <li className="nav-item"><a className="nav-link" href="/tasks">Tasks</a></li>
                <li className="nav-item"><a className="nav-link" href="/recieps">Recipes</a></li>
                <li className="nav-item"><a className="nav-link" href="/whitelist">Whitelist</a></li>
                <li className="nav-item"><a className="nav-link" href="/account">Account</a></li>
                <li className="nav-item"><button className="nav-link" onClick={logout}>Logout</button></li
                ></> : <>
                <li className="nav-item"><a className="nav-link" href="/register">Register</a></li>
                <li className="nav-item"><a className="nav-link" href="/login">Log in</a></li>
            </>}
        </ul>
    </>
    )
}

export default NavBar;
