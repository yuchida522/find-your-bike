'use strict';
function Login() {

	// function will go here
	return (
		<div>
			<h1>Log In</h1>
			<Form.Group controlId="formBasicEmail">
				<Form.Label>Email address</Form.Label>
				<Form.Control type="email" placeholder="Enter email" />
				<Form.Text className="text-muted">
				We'll never share your email with anyone else.
				</Form.Text>
			</Form.Group>

			<Form.Group controlId="formBasicPassword">
				<Form.Label>Password</Form.Label>
				<Form.Control type="password" placeholder="Password" />
			</Form.Group>

			<Button variant="primary">Log In</Button>
			
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
					<Form.Label>Username</Form.Label>
					<Form.Control type="username" placeholder="Enter Username" />
				</Form.Group>

				<Form.Group controlId="formBasicPassword">
					<Form.Label>Password</Form.Label>
					<Form.Control type="password" placeholder="Enter Passsword" />
				</Form.Group>

				<Button variant="primary">Register</Button>

		</div>
	)
}

// class Login extends React.Component  {
// 	constructor(props) {
// 		super(props);
// 	}
// 	render(){
// 		return (
// 			<div>
// 				<h1>Log In</h1>
// 				<Form.Group controlId="formBasicEmail">
// 					<Form.Label>Email address</Form.Label>
// 					<Form.Control type="email" placeholder="Enter email" />
// 					<Form.Text className="text-muted">
// 					We'll never share your email with anyone else.
// 					</Form.Text>
// 				</Form.Group>
	
// 				<Form.Group controlId="formBasicPassword">
// 					<Form.Label>Password</Form.Label>
// 					<Form.Control type="password" placeholder="Password" />
// 				</Form.Group>
	
// 				<Button variant="primary">Log In</Button>
				
// 			</div>
// 		)
// 	}


// 	// function will go here
	
// }


// ReactDOM.render(<Map />, document.getElementById('map'));

