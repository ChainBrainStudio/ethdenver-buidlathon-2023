// import { ThemeProvider } from "@emotion/react";
// import { Button } from "@mui/material";
// import { createTheme } from "@mui/system";
// import { useWeb3React } from "@web3-react/core"
// import { useEffect, useState } from "react";

// import {
//     ADAPTER_EVENTS,
//     ADAPTER_STATUS,
//     CHAIN_NAMESPACES,
//     CustomChainConfig,
//     getChainConfig,
//     SafeEventEmitterProvider,
//     WALLET_ADAPTER_TYPE,
//     WALLET_ADAPTERS,
//     BaseAdapterConfig,
//     CONNECTED_EVENT_DATA,
//     IAdapter,
//     storageAvailable,
//     ADAPTER_CATEGORY,
//   } from "@web3auth/base";
  
//   const clientId="BIxVtq-MJaOUTlnB0CQKyfpt4IXQFOdu1fF8XpVW00bmgMJK0fgSLwdN8xFjsxaEqsyoU_GTnTUexJVhbu5zKUQ"
// const theme = createTheme({
//     status: {
//       danger: '#e53e3e',
//     },
//     palette: {
//       primary: {
//         main: '#f2ebeb',
//         contrastText: '#515151',
//         backgroundColor: "white"
//       }
//     },
//   });

  



//   const renderMetamask = (address) => {
//     if (!address) {
//       return (
//         // <button onClick={() => this.connectToMetamask()}>Connect to Metamask</button>
//         <Button color="primary"  onClick={() => this.connectToMetamask()} sx={[{ "&:hover": { backgroundColor: 'grey' , position: "sticky", top: 0, float: 'right'} }]}>Connect</Button>
//       )
//     } else {
//       return (
//         <Button variant="contained" sx={{ position: "sticky", top: 0}} color="success">
//           Connected
//         </Button>
//       );

//     }
// };


// export default function MetamaskWeb3() {
//     //Initialize within your constructor
//     const [address, setSelectedAddress] =  useState('');
    

//     useEffect(async () => {
//         const web3auth = new web3auth({
//             clientId: "YOUR_WEB3AUTH_CLIENT_ID", // Get your Client ID from Web3Auth Dashboard
//             chainConfig: {
//               chainNamespace: "eip155",
//               chainId: "0x1", // Please use 0x5 for Goerli Testnet
//             },
//           });
//         await web3auth.initModal();
//         const metamaskAdapter = new metamaskAdapter({
//             clientId,
//             sessionTime: 3600, // 1 hour in seconds
//             web3AuthNetwork: "mainnet",
//             chainConfig: {
//               chainNamespace: CHAIN_NAMESPACES.EIP155,
//               chainId: "0x1",
//               rpcTarget: "https://mainnet.infura.io/v3/b9d9c16fcd2e4c1c89934683a92e0ec0", // This is the public RPC we have added, please pass on your own endpoint while creating an app
//             },
//           });
//         web3auth.configureAdapter(metamaskAdapter);
//     }, []);

    
    
//     return(
//         <div>
//           <ThemeProvider theme={theme}>
//           {renderMetamask(address)}
//           </ThemeProvider>
//         </div>
//       )
//   }