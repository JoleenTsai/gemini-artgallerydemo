// game.js - Core physics and interaction logic for the Smash Room

import * as THREE from 'three';
import * as CANNON from 'cannon-es';

export function handleSmashImpact(physObj, impactPoint, camera, scene, world, physicsObjects, materials, defaultMaterial) {
    if (!physObj || !physObj.isBreakable) {
        return;
    }

    physObj.hp -= 25; // Example damage

    if (physObj.hp <= 0) {
        shatterObject(physObj, impactPoint, camera, scene, world, physicsObjects, materials, defaultMaterial);
    }
}

function shatterObject(physObj, impactPoint, camera, scene, world, physicsObjects, materials, defaultMaterial) {
    const shatterType = physObj.shatterType;

    switch (shatterType) {
        case 'glass':
            applyGlassShatterEffect(physObj, impactPoint, camera, scene, world, physicsObjects, materials, defaultMaterial);
            break;
        case 'ceramic':
            applyCeramicShatterEffect(physObj, impactPoint, camera, scene, world, physicsObjects, materials, defaultMaterial);
            break;
        default:
            applyGenericShatterEffect(physObj, impactPoint, camera, scene, world, physicsObjects, materials, defaultMaterial);
            break;
    }

    // Remove the original object from the scene and physics world
    scene.remove(physObj.mesh);
    world.removeBody(physObj.body);

    // Remove from our managed list
    const index = physicsObjects.indexOf(physObj);
    if (index > -1) {
        physicsObjects.splice(index, 1);
    }
}

function applyGlassShatterEffect(physObj, impactPoint, camera, scene, world, physicsObjects, materials, defaultMaterial) {
    const numShards = 10 + Math.floor(Math.random() * 10); // 10-19 shards
    const glassMaterial = materials.bottleClear; // Or choose based on original bottle color

    for (let i = 0; i < numShards; i++) {
        const shardSize = 0.05 + Math.random() * 0.1;
        const shardGeometry = new THREE.BoxGeometry(shardSize, shardSize, shardSize);
        const shardMesh = new THREE.Mesh(shardGeometry, glassMaterial);

        const shardBody = new CANNON.Body({
            mass: 0.1,
            shape: new CANNON.Box(new CANNON.Vec3(shardSize / 2, shardSize / 2, shardSize / 2)),
            position: new CANNON.Vec3(
                physObj.body.position.x + (Math.random() - 0.5) * 0.5,
                physObj.body.position.y + (Math.random() - 0.5) * 0.5,
                physObj.body.position.z + (Math.random() - 0.5) * 0.5
            ),
            material: defaultMaterial
        });

        const forceDirection = new THREE.Vector3().subVectors(shardBody.position, impactPoint).normalize();
        const impulseStrength = 2 + Math.random() * 3;
        const impulse = new CANNON.Vec3(
            forceDirection.x * impulseStrength,
            forceDirection.y * impulseStrength,
            forceDirection.z * impulseStrength
        );

        shardBody.applyImpulse(impulse, shardBody.position);
        
        // Add to world
        scene.add(shardMesh);
        world.addBody(shardBody);

        const tempPhysObj = { mesh: shardMesh, body: shardBody, isBreakable: false };
        physicsObjects.push(tempPhysObj);

        // Remove shards after a while
        setTimeout(() => {
            scene.remove(shardMesh);
            world.removeBody(shardBody);
            const index = physicsObjects.indexOf(tempPhysObj);
            if (index > -1) {
                physicsObjects.splice(index, 1);
            }
        }, 3000 + Math.random() * 2000);
    }
}

function applyCeramicShatterEffect(physObj, impactPoint, camera, scene, world, physicsObjects, materials, defaultMaterial) {
    const numShards = 15 + Math.floor(Math.random() * 10);
    const ceramicMaterial = materials.ceramic;

    for (let i = 0; i < numShards; i++) {
        const shardSize = 0.1 + Math.random() * 0.2;
        const shardGeometry = new THREE.BoxGeometry(shardSize, shardSize, shardSize);
        const shardMesh = new THREE.Mesh(shardGeometry, ceramicMaterial);

        const shardBody = new CANNON.Body({
            mass: 0.2,
            shape: new CANNON.Box(new CANNON.Vec3(shardSize / 2, shardSize / 2, shardSize / 2)),
            position: new CANNON.Vec3(
                physObj.body.position.x + (Math.random() - 0.5),
                physObj.body.position.y + (Math.random() - 0.5),
                physObj.body.position.z + (Math.random() - 0.5)
            ),
            material: defaultMaterial
        });

        const forceDirection = new THREE.Vector3().subVectors(shardBody.position, impactPoint).normalize();
        const impulseStrength = 1 + Math.random() * 4;
        const impulse = new CANNON.Vec3(
            forceDirection.x * impulseStrength,
            forceDirection.y * impulseStrength,
            forceDirection.z * impulseStrength
        );

        shardBody.applyImpulse(impulse, shardBody.position);
        
        scene.add(shardMesh);
        world.addBody(shardBody);
        
        const tempPhysObj = { mesh: shardMesh, body: shardBody, isBreakable: false };
        physicsObjects.push(tempPhysObj);

        setTimeout(() => {
            scene.remove(shardMesh);
            world.removeBody(shardBody);
            const index = physicsObjects.indexOf(tempPhysObj);
            if (index > -1) {
                physicsObjects.splice(index, 1);
            }
        }, 4000 + Math.random() * 2000);
    }
}


function applyGenericShatterEffect(physObj, impactPoint, camera, scene, world, physicsObjects, materials, defaultMaterial) {
    const numShards = 5;
    for (let i = 0; i < numShards; i++) {
        const shardSize = 0.2;
        const shardGeometry = new THREE.BoxGeometry(shardSize, shardSize, shardSize);
        const shardMesh = new THREE.Mesh(shardGeometry, new THREE.MeshStandardMaterial({ color: 0xff0000 }));
        const shardBody = new CANNON.Body({
            mass: 0.1,
            shape: new CANNON.Box(new CANNON.Vec3(shardSize/2, shardSize/2, shardSize/2)),
            position: new CANNON.Vec3(
                physObj.body.position.x + (Math.random() - 0.5),
                physObj.body.position.y + (Math.random() - 0.5),
                physObj.body.position.z + (Math.random() - 0.5)
            ),
            material: defaultMaterial
        });

        const forceDirection = new THREE.Vector3().subVectors(shardBody.position, impactPoint).normalize();
        const impulse = new CANNON.Vec3(forceDirection.x * 2, forceDirection.y * 2, forceDirection.z * 2);
        shardBody.applyImpulse(impulse, shardBody.position);
        
        scene.add(shardMesh);
        world.addBody(shardBody);

        const tempPhysObj = { mesh: shardMesh, body: shardBody, isBreakable: false };
        physicsObjects.push(tempPhysObj);

        setTimeout(() => {
            scene.remove(shardMesh);
            world.removeBody(shardBody);
            const index = physicsObjects.indexOf(tempPhysObj);
            if (index > -1) {
                physicsObjects.splice(index, 1);
            }
        }, 2000);
    }
}
