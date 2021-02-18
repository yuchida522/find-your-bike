'use strict';


function CreateListing () {
	const [uploadImageState, setUploadImageState] = React.useState('');
	const [selectedFile, setSelectedFile] = React.useState('');
	
	const handleUploadImage = (e) => {
		const image = e.target.files[0];
	}
	//functions will go here
	return (
    <React.Fragment>
			<h1>Create Listing</h1>
			<Form onSubmit={handleSubmitForm}>
			<Form.Group>
    		<Form.File id="imageUpload" label="Upload Image"
				 onChange={handleUploadImage} value={uploadImageState}
				className="photo-upload"  />
  		</Form.Group>

			</Form>
    </React.Fragment>
	);
}