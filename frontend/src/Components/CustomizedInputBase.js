import * as React from 'react';
import Paper from '@mui/material/Paper';
import IconButton from '@mui/material/IconButton';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import SearchIcon from '@mui/icons-material/Search';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import InputLabel from '@mui/material/InputLabel';
import axios from 'axios';
import { backend_url } from '../constants';

import {
  apiCalled,
  setData,
} from "../redux/reducers/Counter/counter.actions"
import { connect } from 'react-redux';

const propmts = ["What NFTs are trending in the last week?", "What is the address for the CryptoPunks collection?"]
const prompt = propmts[Math.floor(Math.random()*propmts.length)]



export function CustomizedInputBase(props) {
  const [input, setInput] = React.useState('');
  const [subgraph, setSubgraph] = React.useState('');
  const Search = async (event) => {
    let res;
    event.preventDefault();

    props.apiCalled(true)

    res = await axios.post(`${backend_url}/api/v1/dashboard`, {
      input: input,
      subgraph: subgraph,
    })

    props.setData(res.data?.output);
    props.apiCalled(false);
  }

  const handleChange = (event) => {

    setSubgraph(event.target.value);
  };

  const subgraphs = [{"id": "uniswap-v3", "subgraph": "uniswap-v3"},{"id": "opensea-v2", "subgraph": "opensea-v2"},{"id": "uniswap-governance", "subgraph": "uniswap-governance"},{"id": "aave-governance", "subgraph": "aave-governance"}];
  const ITEM_HEIGHT = 35;
  const ITEM_PADDING_TOP = 8;
  const MenuProps = {
    PaperProps: {
      style: {
        maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      },
    },

  };

  const handleCategoryChange = (event) => {
    setSubgraph(event.target.value);
  };

  return (
    <Paper
      sx={{ p: '2px 4px', display: 'flex', alignItems: 'center', width: "80%", flexGrow: 0, marginTop: "64px" }}
    >
    <Box
      component="form"
      sx={{
         m: 1, width: '100%', display: 'flex'
      }}
      noValidate
      autoComplete="off"
      onSubmit={Search}
    >
      <FormControl sx={{ width:"20%" }}>

      <InputLabel id="sub-graph-label">SubGraph</InputLabel>
       <Select
          labelId="sub-graph-label"
          sx={{  height:"55px", marginRight:"5px"}}
          id="sub-graph"
          value={subgraph}
          label="Subgraph"
          MenuProps={MenuProps}
          onChange={handleCategoryChange}
          // defaultValue={subgraph}
        >
          {subgraphs.map((subgraph_) => (
            <MenuItem value={subgraph_.id}>
              {subgraph_.subgraph}
            </MenuItem>
          ))}
        </Select>
        </FormControl>
      <TextField
        sx={{ width:"75%"}}
        id="outlined-controlled"
        label={prompt}
        value={input}
        onChange={(event) => {
            setInput(event.target.value);
        }}
        noValidate
        autoComplete="off"
        onSubmit={Search}
      />


      <IconButton type="submit" sx={{ p: '10px', width:"5%", marginRight:"0px" }} aria-label="search">
        <SearchIcon onClick={(e) => { Search(e) }} />
      </IconButton>
      </Box>

    </Paper>
  );
}

const mapStateToProps = state => {
  return {
    count: state.counter.count,
    data: state.counter.data
  }
}

const mapDispatchToProps = dispatch => {
  return {
    setData: (data) => dispatch(setData(data)),
    apiCalled: (data) => dispatch(apiCalled(data))
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(CustomizedInputBase)
