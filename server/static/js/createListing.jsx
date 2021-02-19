'use strict';


function CreateListing () {
	// const [uploadImageState, setUploadImageState] = React.useState('');
	const [selectedFile, setSelectedFile] = React.useState('');
	const myWidget = cloudinary.createUploadWidget({cloudName:'onlinebike', upload_preset:'g3w96a71',}, 
						(error, result) => {if (result.event == "success") {
							setSelectedFile(result.info.url)
						}})
	// const handleUploadImage = (e) => {
	// 	const image = e.target.files[0];
	// }
	//functions will go here
	return (
    <React.Fragment>
			<h1>Create Listing</h1>
			<Form>
				<Form.Group as={Row} controlId="listingTitle">
					<Form.Label column sm="2">
						Title
					</Form.Label>
					<Col sm="10">
						<Form.Control type="text" placeholder="Title" />
					</Col>
  			</Form.Group>
				<Form.Group as={Row} controlId="listingPhotos">
					<Form.Label column sm="2">
						Images
					</Form.Label>
					<Col sm="10">
						<Button id="upload-image-btn" onClick={()=> {myWidget.open()}}>Upload Images</Button>
					</Col>
				</Form.Group>
				<Form.Group as={Row} controlId="listingDescription">
					<Form.Label column sm="2">
						Description
					</Form.Label>
					<Col sm="10">
						<Form.Control as="textarea" rows={3} placeholder="Please give us a detailed description of your bike" />
					</Col>
  			</Form.Group>
				<Form.Group as={Row} controlId="listingCondition">
					<Form.Label column sm="2">
						Condition
					</Form.Label>
						<Form.Check inline label="New" type="checkbox" />
						<Form.Check inline label="Used" type="checkbox" />
  			</Form.Group>
				<Form.Group as={Row} controlId="listingType">
					<Form.Label column sm="2">
						Listing Type
					</Form.Label>
						<Form.Check inline label="For sale" type="checkbox" />
						<Form.Check inline label="For trade" type="checkbox" />
						<Form.Check inline label="For free" type="checkbox" />
  			</Form.Group>
				<Form.Group as={Row} controlId="listingPrice">
					<Form.Label column sm="2">
						Price
					</Form.Label>
					<Col sm="7">
						<Form.Control type="text" placeholder="required" />
					</Col>
  			</Form.Group>
					<Row>
						<Form.Label column sm="2">
							Bike Type
						</Form.Label>
						<Col sm="3">
							<Form.Control type="text" placeholder="required" />
						</Col>
						<Form.Label column sm="2">
							Model
						</Form.Label>
						<Col sm="3">
							<Form.Control type="text" placeholder="required" />
						</Col>		
  				</Row>
					<Row>
						<Form.Label column sm="2">
							Brand
						</Form.Label>
						<Col sm="3">
							<Form.Control type="text" placeholder="required" />
						</Col>
						<Form.Label column sm="2">
							Frame type
						</Form.Label>
						<Col sm="3">
							<Form.Control type="text" placeholder="required" />
						</Col>		
  				</Row>
					<Row>
					<Form.Label column sm="2">
						Frame size
					</Form.Label>
					<Col sm="3">
						<Form.Control type="text" placeholder="required" />
					</Col>		
  				</Row>	
				<Form.Group as={Row} id="listingSubmitBtnGroup">
				<Col sm={{ span: 10, offset: 7 }}>
				<Button id="submit-listing-btn" type="submit">Create Listing</Button>
				</Col>	
				</Form.Group>
			</Form>
    </React.Fragment>
	);
}