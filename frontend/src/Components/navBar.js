import { Alert, Button, ClickAwayListener, Snackbar } from '@mui/material';
import AppBar from '@mui/material/AppBar';
import Badge from '@mui/material/Badge';
import Box from '@mui/material/Box';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import Toolbar from '@mui/material/Toolbar';
import * as React from 'react';
import { connect, useDispatch } from 'react-redux';
import { itemSuccess } from '../redux/reducers/Counter/counter.actions';

import Metamask from './Metamask';


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


    <Box sx={{ flexGrow: 1, position: "sticky", top: 0, zIndex:1}}>
      {<Snackbar open={success} autoHideDuration={6000} onClose={handleClose}><Alert severity="success">Connected to Metamask </Alert></Snackbar>}
      
      

      <AppBar position="static" style={{ backgroundColor: "black" }}>
        <Toolbar>
          {/* <HomeIcon onClick={goToHome} sx={{ display: { xs: 'none', sm: 'block', cursor: 'pointer' } }} /> */}
          <Box sx={{ flexGrow: 1 }} />
          <Metamask />

        </Toolbar>
      </AppBar>
      {/* {renderMobileMenu} */}
      {renderMenu}
    </Box>
  );
}
function mapStateToProps(state){
  return {
    //   "data": state.productReducer,
  }
}


export default connect(mapStateToProps)(NavBar)