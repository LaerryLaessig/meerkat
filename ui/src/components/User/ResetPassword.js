import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUnlockAlt } from '@fortawesome/free-solid-svg-icons'

function ResetPassword(props) {
    return (
        <>
            <div>
                <h1 className="mb-0 h4">Reset Password</h1>
                <form>
                    <fieldset className="form-group">
                        <div className="form-group">
                            <label className="form-control-label">Password</label>
                            <div className="input-group">
                                <span className="input-group-text"><FontAwesomeIcon icon={faUnlockAlt} /></span>
                                <input className="form-control form-control-lg"></input>
                            </div>
                        </div>
                        <div className="form-group">
                            <label className="form-control-label">Confirm Password</label>
                            <div className="input-group">
                                <span className="input-group-text"><FontAwesomeIcon icon={faUnlockAlt} /></span>
                                <input className="form-control form-control-lg"></input>
                            </div>
                        </div>
                    </fieldset>
                    <div className="btn-group">
                        <button className="btn btn-outline-info">Change</button>
                    </div>
                </form>
            </div>
        </>
    );
}

export default ResetPassword;