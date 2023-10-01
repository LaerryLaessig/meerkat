import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faEnvelope } from '@fortawesome/free-solid-svg-icons'

function ForgotPassword(props) {
    return (
        <>
            <div>
                <h1 className="mb-0 h4">Reset Password</h1>
                <form method="POST" action="{{ url_for('request_reset_password') }}">
                    <fieldset className="form-group">
                        <div className="form-group">
                            <label className="form-control-label">E-Mail</label>
                            <div className="input-group">
                                <span className="input-group-text"><FontAwesomeIcon icon={faEnvelope} /></span>
                                <input className="form-control form-control-lg"></input>
                            </div>
                        </div>
                    </fieldset>
                    <div className="btn-group">
                        <button className="btn btn-outline-info">Send</button>
                    </div>
                </form>
            </div>
        </>
    );
}

export default ForgotPassword;