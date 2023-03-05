// import logo from './logo.svg';
import { Grid } from '@mui/material';
import './App.css';
import CustomizedInputBase from './Components/CustomizedInputBase';
import ColumnGroupingTable from './Components/table';


function HomeComponent() {
  return (
      <Grid
      className="grid"
      container
      spacing={0}
      direction="column"
      alignItems="center"
      justifyContent="center"
      style={{ minHeight: '100vh' }}>

      <CustomizedInputBase />
      <ColumnGroupingTable/>
      </Grid>
  );
}


export default HomeComponent;
