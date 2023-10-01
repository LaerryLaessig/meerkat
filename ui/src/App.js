import { BrowserRouter, Route, Routes } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import Login from './components/User/Login'
import Home from './components/Home'
import Tasks from './components/Tasks/Tasks';
import Recieps from './components/Recieps/Recieps';
import Whitelist from './components/Admin/Whitelist';
import Account from './components/User/Account';
import Register from './components/User/Register';
import ForgotPassword from './components/User/ForgotPassword';
import ResetPassword from './components/User/ResetPassword'
import Explaination from './components/Explaination';
import NavBar from './components/NavBar'
import AuthHandler from './core/AuthHandler'
import './App.css'

function App() {
  const { token, removeToken, setToken, hasJWT } = AuthHandler();

  return (
    <BrowserRouter>
      <div className="App">
        <NavBar token={removeToken} />
        {!token && token !== "" && token !== undefined ?
          <>
            <Routes>
              <Route exact path="/" element={<Explaination></Explaination>}></Route>
              <Route exact path="/login" element={<Login setToken={setToken} />}></Route>
              <Route exact path="/register" element={<Register></Register>}></Route>
              <Route exact path="/forgotpassword" element={<ForgotPassword></ForgotPassword>}></Route>
              <Route exact path="/resetpassword" element={<ResetPassword></ResetPassword>}></Route>
            </Routes>
          </>
          : (
            <>
              <Routes>
                <Route exact path="/login" element={<Home></Home>}></Route>
                <Route exact path="/home" element={<Home></Home>}></Route>
                <Route exact path="/tasks" element={<Tasks tokeb={token} setToken={setToken}></Tasks>}></Route>
                <Route exact path="/recieps" element={<Recieps tokeb={token} setToken={setToken}></Recieps>}></Route>
                <Route exact path="/whitelist" element={<Whitelist tokeb={token} setToken={setToken}></Whitelist>}></Route>
                <Route exact path="/account" element={<Account tokeb={token} setToken={setToken}></Account>}></Route>
              </Routes>
            </>
          )}
      </div>
    </BrowserRouter>
  );
}

export default App;
