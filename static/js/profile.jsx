'use strict';

function Profile() {

	return (
		<React.Fragment>
			<Container>
				<Row>
				<h1>Find Your Bike</h1>
				search
				<input type="text"></input> <br/>
				</Row>
			</Container>
			<Container>
				<Row>
					<Col xs={6} md={4}>
						<Image src="static/img/IMG-2719.JPG" thumbnail/>
					</Col>
				</Row>
			</Container>		
			
		</React.Fragment>
	)
}