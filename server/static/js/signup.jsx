const RegistrationForm = (props) => {
function Signup(){
    return (
        <div>
            <h1>Register Now!</h1>
            <Form>
            <Form.Group controlId="formBasicFname">
                <Form.Label>First name</Form.Label>
                <Form.Control type="fname" placeholder="Enter First Name" />
            </Form.Group>
            <Form.Group controlId="formBasicLname">
                <Form.Label>Last Name</Form.Label>
                <Form.Control type="Lname" placeholder="Enter Last Name" />
            </Form.Group>
            <Form.Group controlId="formBasicEmail">
                <Form.Label>Email address</Form.Label>
                <Form.Control type="email" placeholder="Enter email" />
            </Form.Group>
            <Form.Group controlId="formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control type="password" placeholder="Password" />
            </Form.Group>
            <Form.Group controlId="formBasicPhoneNumber">
                <Form.Label>Phone Number</Form.Label>
                <Form.Control type="PhoneNumber" placeholder="Enter Phone Number" />
            </Form.Group>
            <Button variant="primary" type="submit">
                Submit
            </Button>
            </Form>
        </div>
    ) 
}
}

// const RegistrationForm = props => {
//     // array destructuring -- two vars declared inside of an array-- 
//     // react,usestate returns an array with two things in them. We pull them out into 2 diff vars
//     const [state, makeState] = React.useState(
//         {login: false,
//         user: {},
//         email: "",
//         password: "",
//         lname: "",
//         fname: ""   
//         }
//     );
//     // what is passed into the use state is what you are initializing your state with. 
//         // Here it should be everything you need for someone to log in 
//     // state is the current state of the registration??
//     // useState is a function that will update the reigstration statuse??
// }

// const registerChange = (e) => {

    
// }
// const registerChange = (e) => {
    
// }
    
