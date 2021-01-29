'use strict';

function NavComponent() {
	return (
		<Navbar id="navbar" bg="dark" sticky="top">
            <Navbar.Brand href="#">Online Bike Exchange</Navbar.Brand>
			<Nav id="nav" className="mr-auto">
                <Nav.Link href="home">Home</Nav.Link>
                <Nav.Link href="favorites">Favorites</Nav.Link>
                <Nav.Link href="search">Search</Nav.Link>
                <Nav.Link href="profile">Profile</Nav.Link>
                <Nav.Link href="about">About</Nav.Link>
                <Nav.Link href="login">Login</Nav.Link>
                <Nav.Link href="logout">Sign Out</Nav.Link>
			</Nav>
		</Navbar>
	)
}