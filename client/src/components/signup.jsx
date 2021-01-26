const RegistrationForm = props => {
    // array destructuring -- two vars declared inside of an array-- 
    // react,usestate returns an array with two things in them. We pull them out into 2 diff vars
    const [state, makeState] = React.useState(
        {login: false,
        user: {},
        email: "",
        password: "",
        lname: "",
        fname: ""   
        }
    );
    // what is passed into the use state is what you are initializing your state with. 
        // Here it should be everything you need for someone to log in 
    // state is the current state of the registration??
    // useState is a function that will update the reigstration statuse??
}

const registerChange = (e) => {
    