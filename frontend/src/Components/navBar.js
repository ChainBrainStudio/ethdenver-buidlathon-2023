import { Alert, Button, ClickAwayListener, Snackbar, Typography } from '@mui/material';
import AppBar from '@mui/material/AppBar';
import Badge from '@mui/material/Badge';
import logo from '../images/logo_1.png';
import name from '../images/name_1.png';
import Box from '@mui/material/Box';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import Toolbar from '@mui/material/Toolbar';
import * as React from 'react';
import { connect, useDispatch } from 'react-redux';
import { itemSuccess } from '../redux/reducers/Counter/counter.actions';

import Metamask from './Metamask';
import MetamaskWeb3 from './Metamask-web3';


function NavBar(props) {
  
  const dispatch = useDispatch();
//   React.useEffect(()=>{
//       dispatch(fetchCategories({"value": "", "category": 0 }));
//   }, [])

  const success = props.data?.success
  ? props.data?.success
  : false;

  const [anchorEl, setAnchorEl] = React.useState(null);
  const [anchorPopperEl, setAnchorPopperEl] = React.useState(null);
  const [mobileMoreAnchorEl, setMobileMoreAnchorEl] = React.useState(null);
  const [openPopper, setOpenPopper] = React.useState(false);
  
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);


  const isMenuOpen = Boolean(anchorEl);
  const isMobileMenuOpen = Boolean(mobileMoreAnchorEl);

  const handleProfileMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMobileMenuClose = () => {
    setMobileMoreAnchorEl(null);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
    handleMobileMenuClose();
  };



  const menuId = 'primary-search-account-menu';
    const renderMenu = (
    <Menu
      anchorEl={anchorEl}
      anchorOrigin={{
        vertical: 'top',
        horizontal: 'right',
      }}
      id={menuId}
      keepMounted
      transformOrigin={{
        vertical: 'top',
        horizontal: 'right',
      }}
      open={isMenuOpen}
      onClose={handleMenuClose}
    >
    </Menu>
  );

  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    dispatch(itemSuccess(false));
  };


  return (


    <Box sx={{ position: "fixed", top: 0, width:"100%", zIndex:"10000"}}>
      
      
      {/* <AppBar > */}
        <Toolbar position="fixed" style={{ backgroundColor: "black"  }}>
          {/* <HomeIcon onClick={goToHome} sx={{ display: { xs: 'none', sm: 'block', cursor: 'pointer' } }} /> */}
          {/* <img src={logo} width={100} height={64}/> */}
          <Box
        component="img"
        sx={{
          height: 64,
          width: 64,
          paddingTop:"10px"
        }}
        alt="logo"
        src={logo}
      />
      <Typography variant="h6" color='#701ea5' fontFamily="Gill Sans" paddingTop="10px" gutterBottom>
        CHAINBRAIN
      </Typography>
          <Box sx={{ flexGrow: 1 }} />
          <Metamask />
          {/* <MetamaskWeb3/> */}
        </Toolbar>
      {/* </AppBar> */}
    </Box>
  );
}
function mapStateToProps(state){
  return {
      "success": state.counter.success,
  }
}


export default connect(mapStateToProps)(NavBar)