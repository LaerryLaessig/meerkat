import { useState } from 'react';

function AuthHandler() {

  function getToken() {
    const userToken = localStorage.getItem('token');
    return userToken && userToken
  }

  const [token, setToken] = useState(getToken());

  function saveToken(userToken) {
    localStorage.setItem('token', userToken);
    setToken(userToken);
  };

  function removeToken() {
    localStorage.removeItem("token");
    setToken(null);
  }

  function hasJWT() {
    let flag = false;

    localStorage.getItem("token") ? flag = true : flag = false

    return flag
  }

  return {
    setToken: saveToken,
    token,
    removeToken,
    hasJWT
  }

}

export default AuthHandler;