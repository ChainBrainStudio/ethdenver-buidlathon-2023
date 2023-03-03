import React, { Component, useEffect, useState } from 'react';
import { ethers } from "ethers";
import { Button } from '@mui/material';
import { useSnackbar } from 'notistack';

import { createTheme, ThemeProvider } from '@mui/material/styles';
import { connect, useDispatch } from 'react-redux';
import { SUCCESS } from '../redux/reducers/Counter/counter.types';
import { itemSuccess } from '../redux/reducers/Counter/counter.actions';

const theme = createTheme({
  status: {
    danger: '#e53e3e',
  },
  palette: {
    primary: {
      main: '#f2ebeb',
      contrastText: '#515151',
      backgroundColor: "white"
    }
  },
});

function Metamask (props){
  const dispatch = useDispatch();
  const  [selectedAddress, setSelectedAddress] = useState("");
  const  [connected, setConnected] = useState("");
  const  [balance, setBalance] = useState("");
  const [haveMetamask, sethaveMetamask] = useState(false);
  const { enqueueSnackbar } = useSnackbar();
  const connectToMetamask = async ()=> {
    if (haveMetamask){
    try{
    const provider = new ethers.providers.Web3Provider(window.ethereum)
    const accounts = await provider.send("eth_requestAccounts", []);
    const balance = await provider.getBalance(accounts[0]);
    const balanceInEther = ethers.utils.formatEther(balance);
    setSelectedAddress(accounts[0]);
    setConnected(true)
    if(accounts[0]){
      enqueueSnackbar('Connected to Metamask');
    }
    setBalance(balanceInEther);}
    catch{
      setConnected(false)
    }
  }
    else{
      enqueueSnackbar('Download metamask extension to connect your wallet');
    }
  }
  
  

    // <div>
        // <p>Welcome {this.state.selectedAddress}</p>
        // <p>Your ETH Balance is: {this.state.balance}</p>
        // </div>
  useEffect(() => {
    const { ethereum } = window;
    const checkMetamaskAvailability = () => {
      if (!ethereum) {
        sethaveMetamask(false);
      }
      sethaveMetamask(true);
    };
    checkMetamaskAvailability();
  }, []);

  const renderMetamask = () => {
    if (!connected) {
      return (
        
        // <button onClick={() => this.connectToMetamask()}>Connect to Metamask</button>
        <Button color="primary"  onClick={connectToMetamask} sx={[{ "&:hover": { backgroundColor: 'grey' , position: "sticky", top: 0, float: 'right'} }]}>Connect</Button>
      )
    } else {
      return (
        <Button variant="contained" sx={{ position: "sticky", top: 0}} color="success">
          Connected
        </Button>
      );
    }
  }
  
    return(
      <div>
        <ThemeProvider theme={theme}>
        {renderMetamask()}
        </ThemeProvider>
      </div>
    )
}



export default Metamask;