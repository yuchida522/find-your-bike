"use strict"

function Register(){
    return(
        <div>
            <h5>New user? Regiseter here!</h5>
				<Form.Group controlId="formBasicName">
					<Form.Label>First Name</Form.Label>
					
					<Form.Control type="Fname" placeholder="Enter First Name" />
				</Form.Group>

				<Form.Group controlId="formBasicName">
					<Form.Label>Last Name</Form.Label>
					<Form.Control type="Lname" placeholder="Enter Last Name" />
				</Form.Group>

				<Form.Group controlId="formBasicUsername">
					<Form.Label>Add Username</Form.Label>
					<Form.Control type="username" placeholder="Enter Username" />
				</Form.Group>

				<Form.Group controlId="formBasicPassword">
					<Form.Label>Password</Form.Label>
					<Form.Control type="password" placeholder="Enter Passsword" />
				</Form.Group>

				<Button variant="primary">Register</Button>
        </div>
    );

}

const RegisterForm = (props) => {
	const [state, setState] = React.setState({
		login: false,
		user: {},
		fname: "",
		lname: "",
		email: "",
		password: ""
	});
}