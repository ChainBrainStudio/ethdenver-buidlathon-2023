import { SETDATA, API_CALLED } from './counter.types';


const INITIAL_STATE = {

   isLoading: false,
    data: ""
};

const reducer = (state = INITIAL_STATE, action) => {

    switch (action.type) {

        case SETDATA:

           return {

             ...state, 
             data: action.data,

           };
         
      case API_CALLED :  
         return {
             ...state,
             isLoading: action.data
         };
         break;

        

      default: return state;

    }

};

export default reducer;