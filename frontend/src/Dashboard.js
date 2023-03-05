// import logo from './logo.svg';
import { CircularProgress, Grid } from '@mui/material';
import axios from 'axios';
import { useSnackbar } from 'notistack';
import { useEffect, useState } from 'react';
import { connect } from 'react-redux';
import './App.css';
import CustomizedInputBase from './Components/CustomizedInputBase';
import DashboardHelper from './Components/dashboardHelper';
import ColumnGroupingTable from './Components/table';
import { backend_url } from './constants';

function DashboardComponent(props) {
  const [ isLoading, setisLoading] = useState(false)
  const {wallet_address} = props;
  const [res, setres] = useState("");
  
  // const saveDashboard = async ()=>{

  //   try{
  //     set_sending_request("true")
  //     const res = await axios.post(`${backend_url}/api/v1/dashboard/${data?.id}`, {
  //     wallet_address: wallet_address,
  //   })
  //   // enqueueSnackbar('Saved Dashboard');
  //   set_sending_request(false)
  // }
  //   catch{
  //     set_sending_request(false)
  //     enqueueSnackbar('Server error!!');
  //   }
  // }
  const { enqueueSnackbar } = useSnackbar();
    const getData = async ()=>{
      if(wallet_address){
    try{
      setisLoading(true)
      // set_sending_request("true")
      const response = await axios.get(`${backend_url}/api/v1/dashboard/user/${wallet_address}`)
      setres(response)
    //  if(res){
    //   if (res.data.length  ===0){
    //     enqueueSnackbar('No saved dashboards');
    //   }
    //   else{
    //     enqueueSnackbar('Fetched Dashboards');
    //   }}
      setisLoading(false)
  }
    catch(error){
      console.log(error)
      setisLoading(false)
      enqueueSnackbar('Retrieving data failed!!');
    }
  }}

  // const getDashBoardData = async() => {
  //   const { tableData, setTableData } = useState("");

  // }
  

  useEffect(() => {
    getData()
  }, [wallet_address]);
  if(isLoading){
    return (
      <CircularProgress sx={{ align: 'center', marginTop:"10px",} }  color="secondary"/>
  )}
  else{
  return (
    <Grid
    className="grid"
    container
    spacing={0}
    direction="column"
    alignItems="center"
    justifyContent="center"
    style={{ minHeight: '100vh', marginTop:"74px" }}>
     { res?.data && res.data.map((data) => (
        <DashboardHelper data={data.data} user_input={data.user_input} chatgpt_gql={data.chatgpt_gql}/>
      ))}
    
    </Grid>
  );
}}
const mapStateToProps = state => {
  return {
    wallet_address: state.counter.wallet_address,
  }
}
export default connect(mapStateToProps)(DashboardComponent);
